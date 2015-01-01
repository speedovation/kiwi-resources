<?php
/**
 * Whoops - php errors for cool kids
 * @author Filipe Dobreira <http://github.com/filp>
 */

namespace Whoops;
use Whoops\Handler\HandlerInterface;
use Whoops\Exception\ErrorException;
use InvalidArgumentException;
use Exception;

class Run
{
    const EXCEPTION_HANDLER = "handleException";


    public $isRegistered;
    private $sendOutput      = true;
    protected $sendHttpCode    = 500;

    /**
     * @var HandlerInterface[]
     */
    protected $handlerStack = array();


    /**
     * Pushes a handler to the end of the stack
     *
     * @throws InvalidArgumentException If argument is not callable or instance of HandlerInterface
     * @param  Callable|HandlerInterface $handler
     * @return Run
     */
    public function pushHandler($handler)
    {
        if(is_callable($handler)) {
            $handler = new CallbackHandler($handler);
        }

        if(!$handler instanceof HandlerInterface) {
            throw new InvalidArgumentException(
                  "Argument to " . __METHOD__ . " must be a callable, or instance of"
                . "Whoops\\Handler\\HandlerInterface"
            );
        }

        $this->handlerStack[] = $handler;
        return $this;
    }

 
 
    private static function isLevelFatal($level)
    {
        return in_array(
            $level,
            array(
                E_ERROR,
                E_PARSE,
                E_CORE_ERROR,
                E_CORE_WARNING,
                E_COMPILE_ERROR,
                E_COMPILE_WARNING
            )
        );
    }
}
